# Mobile Applications - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/visual-builder/mobile-apps  
**Scraped:** 2025-12-10 14:03:13

**Description:** Build native iOS and Android apps with React Native. Live preview and code export.

---

Mobile Applications - AlgorithmShift Documentation | AlgorithmShiftDocumentationApp Builder
# Mobile Applications

Build native iOS and Android applications with the same visual builder. Live mobile preview and React Native code export.

### React Native

True native apps

### Live Preview

See changes instantly

### Code Export

Full RN project

### App Stores

Deploy to stores

## Mobile Component System

Build mobile apps with 21 native React Native components, fully integrated into the visual builder. Drag, drop, and configure—no React Native knowledge required.

### What Makes This Different?

Unlike web builders that add a "mobile responsive" view, AlgorithmShift generates actual React Native code using native mobile components. This means:

- • True native performance (not a WebView)
- • Platform-specific UI (iOS vs Android differences)
- • Access to native device features (camera, GPS, notifications)
- • Publish to Apple App Store and Google Play

### 21 Native Components Available

#### Layout & Container
`View``ScrollView``SafeAreaView``KeyboardAvoidingView`
#### Input & Interaction
`TextInput``TouchableOpacity``Pressable``Switch``Button`
#### Display & Media
`Text``Image``ActivityIndicator``StatusBar`
#### Lists & Data
`FlatList``SectionList``RefreshControl`
#### Modals & Overlays
`Modal``Alert`
#### Platform-Specific
`Dimensions``Platform``StyleSheet`[View Complete Component Reference →](https://www.algorithmshift.ai/docs/mobile/components)
## Mobile App Preview

Test your mobile app in real-time with two preview modes: Canvas Preview (instant, in-browser) and QR Code Preview (on your actual device).

### Canvas Preview (React Native Web)

Live preview directly in the builder canvas using React Native Web. See changes instantly as you drag and drop components.

- Instant updates (no build step)
- Mobile viewport simulation
- Great for rapid iteration

### QR Code Preview (Real Device)

Scan a QR code to test your app on your actual phone/tablet. Powered by Expo and Fargate for production-grade preview.

- Test on iOS and Android
- True native performance
- Device-specific testing (gestures, sensors)
[Learn About Mobile Preview →](https://www.algorithmshift.ai/docs/mobile/preview)
## React Native Code Export

### Complete Expo Project

Export a complete, ready-to-run Expo project with all dependencies, navigation, and app configuration. Customize locally or publish directly.
Copy
```
# Download and extract your exported project
unzip MyApp-mobile.zip
cd MyApp-mobile

# Install dependencies
npm install

# Run on iOS simulator
npm run ios

# Run on Android emulator
npm run android

# Build for production
eas build --platform ios
eas build --platform android

# Submit to app stores
eas submit --platform ios
eas submit --platform android
```

## App Store Deployment

### Apple App Store

- Apple Developer Program ($99/year)
- TestFlight beta testing
- 1-3 day review process

### Google Play Store

- Google Play Console ($25 one-time)
- Internal testing tracks
- Few hours review
