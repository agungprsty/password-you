#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dependency_injector.containers as containers
import dependency_injector.providers as providers

class ConfigContainer(containers.DeclarativeContainer):
    config = providers.Configuration('config')