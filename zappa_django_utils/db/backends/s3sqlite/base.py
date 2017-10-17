from django.db.backends.sqlite3.base import DatabaseWrapper

from io import BytesIO

import boto3
import botocore
import logging
import os
import subprocess

class DatabaseWrapper(DatabaseWrapper):
    """
    Wraps the normal Django S3 DB engine in an S3 backer!

    """

    def load_remote_db(self):
        """
        Load remote S3 DB
        """

        signature_version = self.settings_dict.get("SIGNATURE_VERSION", "s3v4")
        s3 = boto3.resource('s3',
                config=botocore.client.Config(signature_version=signature_version))

        if '/tmp/' not in self.settings_dict['NAME']:
            try:
                obj = s3.Object(self.settings_dict['BUCKET'], self.settings_dict['NAME'])
                obj_bytes = obj.get()["Body"] # Will throw E on 404

                with open('/tmp/' + self.settings_dict['NAME'], 'wb') as f:
                    f.write(obj_bytes.read())

            except botocore.exceptions.ClientError as e:
                logging.debug("Couldn't load remote DB object.")
            except Exception as e:
                # Weird one
                logging.debug(e)

        # SQLite DatabaseWrapper will treat our tmp as normal now
        # Check because Django likes to call this function a lot more than it should
        if '/tmp/' not in self.settings_dict['NAME']:
            self.settings_dict['REMOTE_NAME'] = self.settings_dict['NAME']
            self.settings_dict['NAME'] = '/tmp/' + self.settings_dict['NAME']

        # Make sure it exists if it doesn't yet
        if not os.path.isfile(self.settings_dict['NAME']):
            open(self.settings_dict['NAME'], 'a').close()

        logging.debug("Loaded remote DB!")


    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.load_remote_db()

    def close(self, *args, **kwargs):
        """
        Engine closed, copy file to DB
        """
        super(DatabaseWrapper, self).close(*args, **kwargs)

        signature_version = self.settings_dict.get("SIGNATURE_VERSION", "s3v4")
        s3 = boto3.resource('s3',
                config=botocore.client.Config(signature_version=signature_version))

        try:
            with open(self.settings_dict['NAME'], 'rb') as f:
                fb = f.read()
                bytesIO = BytesIO()
                bytesIO.write(fb)
                bytesIO.seek(0)

                s3_object = s3.Object(self.settings_dict['BUCKET'], self.settings_dict['REMOTE_NAME'])
                result = s3_object.put('rb', Body=bytesIO)

        except Exception as e:
            print(e)

        logging.debug("Saved to remote DB!")
