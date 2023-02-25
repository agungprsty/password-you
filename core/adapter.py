#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dependency_injector.containers as containers
import dependency_injector.providers as providers
from core.config import ConfigContainer
from src.adapter.amqp.connection import Connection as AMQPConnection
from src.adapter.amqp.producer import Producer as AMQPProducer
from src.adapter.s3.s3 import S3 as S3GatewayAdapter

class AdapterContainer(containers.DeclarativeContainer):
    crpytor = providers.Singleton(
        Cryptor,
        config=ConfigContainer.config.SECURITY,
    )