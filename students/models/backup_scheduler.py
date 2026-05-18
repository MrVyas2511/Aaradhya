from odoo import models, fields, api
import os
import subprocess
from datetime import datetime

class BackupScheduler(models.Model):
    _name = 'backup.scheduler'

    def backup_database(self, database_name, backup_dir):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = f"{database_name}_{timestamp}.dump"

        try:
            # Use pg_dump to create a backup of the database
            subprocess.run(['pg_dump', '-Fc', database_name, '-f', os.path.join(backup_dir, backup_file)], check=True)
            print(f"Backup created successfully: {backup_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating backup: {e}")

    @api.model
    def _cron_backup_database(self):
        database_name = "RD_1"
        backup_dir = "/home/odoo"

        # Create backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Perform database backup
        self.backup_database(database_name, backup_dir)

