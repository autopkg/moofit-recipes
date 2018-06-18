#!/bin/bash

# Install Xcode components from Xcode.app
/usr/sbin/installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/MobileDevice.pkg -target / -verbose
/usr/sbin/installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/MobileDeviceDevelopment.pkg -target / -verbose
/usr/sbin/installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/XcodeSystemResources.pkg -target / -verbose

# Stop and remove LaunchDaemon and script
/bin/launchctl stop uk.co.moof-it.Xcode.components.plist
/bin/launchctl remove uk.co.moof-it.Xcode.components.plist
rm /tmp/uk.co.amsys.Xcode.components.plist
rm /tmp/componentsInstaller.sh
