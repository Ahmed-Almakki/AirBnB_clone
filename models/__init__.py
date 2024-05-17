#!/usr/bin/python3
""" Script to init"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
