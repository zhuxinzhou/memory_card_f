from flask import Flask
from flask_script import Server,Manager
from jobs.launcher import runJob
from appf import app,manager
from jobs.launcher import runJob



#job entrance
manager.add_command('runjob', runJob() )

def main():
    manager.run( )
()

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc