#!/usr/bin/env python
"""Load all aff4 objects in order to populate the registry.
"""
# pylint: disable=unused-import
from grr_response_server.aff4_objects import aff4_grr
from grr_response_server.aff4_objects import collects
from grr_response_server.aff4_objects import cronjobs
from grr_response_server.aff4_objects import filestore
from grr_response_server.aff4_objects import security
from grr_response_server.aff4_objects import standard
from grr_response_server.aff4_objects import stats
from grr_response_server.aff4_objects import stats_store
from grr_response_server.aff4_objects import user_managers
from grr_response_server.aff4_objects import users
