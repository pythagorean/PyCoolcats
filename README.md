# Coolcats
**Python port of Clutter, a fully distributed social messaging app built on Holochain**

See https://github.com/holochain/clutter for the code that is being ported.

This is a work in progress. It can be built and tested and it works the same as clutter.

To compile the Python for Holochain and React, you will first need to install
[Transcrypt](https://www.transcrypt.org) and [Paver](https://pythonhosted.org/Paver).

    pip install transcrypt
    pip install paver

Just run 'make' and it should build the Zome.

Then go into ui-src and run 'npm install' or 'yarn', followed by 'npm build' or
'yarn build' to compile and install the ui.

If you don't understand what this is about, please see the clutter page linked above.

Not for any sort of production use whatsoever, no warrantee express or implied.
