Pythonista Standalone Project Template
======================================

This project contains everything that is needed to build standalone iOS apps
from scripts written in [Pythonista][1] on iOS.

In order to run your apps on an actual device, you need to be a paying member of
the [iOS Developer Program][2]. You also need to have Xcode and the latest iOS SDK installed.

The first time you build the project, an additional library will be downloaded
automatically (around 15 MB), so the first build will take a little longer.

The file `Script.py` contains the actual script that is executed when running
the app, everything else is basically boilerplate. When you export a project
from the Pythonista app, this will contain the script that you wrote, the
template on GitHub contains one of the sample scripts that ship with Pythonista.

[1]: http://omz-software.com/pythonista
[2]: https://developer.apple.com/programs/ios/