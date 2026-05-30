"""py2app build script for FlowLocal.

Build a proper .app bundle in ALIAS mode (references the existing venv instead of
copying torch/mlx/transformers — fast and reliable):

    cd ~/flow-local && .venv/bin/python setup.py py2app -A

Produces: ~/flow-local/dist/FlowLocal.app
"""
from setuptools import setup

setup(
    app=["flow.py"],
    name="FlowLocal",
    options={
        "py2app": {
            "argv_emulation": False,
            "plist": {
                "CFBundleName": "FlowLocal",
                "CFBundleDisplayName": "FlowLocal",
                "CFBundleIdentifier": "com.flowlocal.app",
                "CFBundleVersion": "1.0",
                "CFBundleShortVersionString": "1.0",
                "LSUIElement": True,  # menu-bar only, no Dock icon
                "NSMicrophoneUsageDescription":
                    "FlowLocal transcribes your speech locally to type what you say.",
            },
        }
    },
)
