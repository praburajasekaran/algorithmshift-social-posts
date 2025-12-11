# React Native Setup - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/react-native  
**Scraped:** 2025-12-10 14:03:23

**Description:** Set up React Native development environment for building native mobile apps.

---

React Native Setup - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# React Native Setup

Set up your development environment for React Native mobile app development.

### For iOS Development

- macOS computer
- Xcode (latest version)
- CocoaPods
- iOS Simulator

### For Android Development

- Windows, macOS, or Linux
- Android Studio
- Android SDK
- Android Emulator

## Running the App

#### iOS
Copy
```
# Install dependencies
npm install

# Install iOS pods
cd ios && pod install && cd ..

# Run on iOS simulator
npm run ios

# Or specific simulator
npm run ios --simulator="iPhone 14 Pro"
```

#### Android
Copy
```
# Install dependencies
npm install

# Start Metro bundler
npm start

# Run on Android emulator
npm run android

# Or on connected device
adb devices
npm run android --device
```
