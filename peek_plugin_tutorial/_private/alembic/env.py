from peek_plugin_base.storage.AlembicEnvBase import AlembicEnvBase

from peek_plugin_tutorial._private.storage import DeclarativeBase

DeclarativeBase.loadStorageTuples()

alembicEnv = AlembicEnvBase(DeclarativeBase.DeclarativeBase.metadata)
alembicEnv.run()