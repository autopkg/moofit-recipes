#!/bin/bash

# Install Xcode components from Xcode.app
installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/MobileDevice.pkg -target / -verbose
installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/MobileDeviceDevelopment.pkg -target / -verbose
installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/XcodeSystemResources.pkg -target / -verbose

# Stop and remove LaunchDaemon and script
launchctl stop uk.co.amsys.Xcode.components.plist
launchctl remove uk.co.amsys.Xcode.components.plist
rm /tmp/uk.co.amsys.Xcode.components.plist
rm /tmp/componentsInstaller.sh
