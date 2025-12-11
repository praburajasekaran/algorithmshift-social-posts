# Mobile Apps - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile  
**Scraped:** 2025-12-10 14:02:35

**Description:** Build native iOS and Android applications with React Native. Visual builder with live mobile preview.

---

Mobile Apps - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# Mobile App Development

Build native iOS and Android applications using React Native. Use the same visual builder, with live mobile preview and automatic code generation.

### React Native

Native iOS & Android

### Live Preview

See changes instantly

### Code Export

Full React Native project

### App Store Ready

Deploy to stores

## Why React Native?

React Native allows you to build truly native applications using JavaScript and React:

### Native Performance

- Real native components (not web views)
- 60 FPS smooth animations
- Platform-specific optimizations
- Native module integration

### Cross-Platform

- Single codebase for iOS and Android
- Shared business logic
- Platform-specific customization
- Faster development & updates

## Mobile Components

When you select "Mobile App", the component library changes to React Native components:

### Core Components

View

Container component
`<View>`
Text

Text display
`<Text>`
TouchableOpacity

Touchable button
`<TouchableOpacity>`
TextInput

Form input
`<TextInput>`
ScrollView

Scrollable content
`<ScrollView>`
FlatList

Optimized list
`<FlatList>`
Image

Image display
`<Image>`
Switch

Toggle switch
`<Switch>`
Modal

Popup dialog
`<Modal>`
### Component Mapping

How web components translate to mobile
Web ComponentReact NativeNotes`div, Container``View`Basic container`Button``TouchableOpacity`Pressable element`p, span, h1-h6``Text`All text must be in Text`input``TextInput`Form input`Table``FlatList`Optimized rendering
## Building a Mobile App
1
### Create Mobile App

When creating an app, select "Mobile App" type:
Copy
```
// App configuration
{
  "name": "My Mobile App",
  "type": "mobile",  // ← Important!
  "description": "iOS and Android app",
  "status": "development"
}
```
2
### Design with Mobile Components

The component library automatically shows mobile components:
Copy
```
// Example: Login Screen
<View style={styles.container}>
  <Text style={styles.title}>Welcome Back</Text>
  
  <TextInput
    placeholder="Email"
    keyboardType="email-address"
    autoCapitalize="none"
  />
  
  <TextInput
    placeholder="Password"
    secureTextEntry={true}
  />
  
  <TouchableOpacity 
    style={styles.button}
    onPress={handleLogin}
  >
    <Text style={styles.buttonText}>Login</Text>
  </TouchableOpacity>
</View>
```
3
### Live Mobile Preview

Click the "App" preview button to see your app in mobile format:

Canvas Dimensions

- • Width: 375px
- • Height: 812px
- • iPhone X/11/12/13 Pro size
- • Black background (simulates device)

React Native Web

- • Components rendered with RN Web
- • Real React Native styling
- • Accurate preview
- • Instant updates
4
### Connect to Data

Mobile apps use the same APIs as web apps:
Copy
```
// FlatList with API data
<FlatList
  data={tasks}
  renderItem={({ item }) => (
    <View style={styles.taskItem}>
      <Text style={styles.taskTitle}>{item.title}</Text>
      <Text style={styles.taskStatus}>{item.status}</Text>
    </View>
  )}
  keyExtractor={item => item.id}
  refreshing={loading}
  onRefresh={loadTasks}
/>

// API call
const loadTasks = async () => {
  const response = await fetch(
    'https://api.algorithmshift.ai/api/v1/tables/tasks',
    {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    }
  );
  const data = await response.json();
  setTasks(data.data);
};
```
5
### Export & Test

Export your app as a complete React Native project:
Copy
```
// Click "Export Code" button
// Downloads: my-mobile-app.zip

// Project structure:
my-mobile-app/
├── App.js
├── package.json
├── app.json
├── metro.config.js
├── babel.config.js
├── android/
├── ios/
└── src/
    ├── screens/
    ├── components/
    ├── navigation/
    ├── services/
    └── styles/

// Run locally
npm install
npm run android  // or npm run ios
```

## Testing Your Mobile App

Multiple ways to test your mobile application:

### Expo Go

Test instantly on your phone:

1. 1. Install Expo Go app
1. 2. Scan QR code from builder
1. 3. App loads on your device
1. 4. Hot reload on changes

### Simulators

Use iOS Simulator or Android Emulator:
Copy
```
# iOS Simulator (macOS only)
npm run ios

# Android Emulator
npm run android
```

### TestFlight / Play Store Beta

Distribute to testers:

- • Build production app
- • Upload to TestFlight (iOS)
- • Upload to Play Store Beta (Android)
- • Invite testers

### Over-the-Air Updates

Push updates without app store approval:

- • Update JavaScript instantly
- • No app store delay
- • Fix bugs quickly
- • Gradual rollout

## Deployment to App Stores

### Apple App Store

1. 1.Enroll in Apple Developer Program ($99/year)
1. 2.Create App ID and certificates
1. 3.Build with eas build --platform ios
1. 4.Submit to App Store Connect
1. 5.Wait for review (1-3 days)

### Google Play Store

1. 1.Register Google Play Console ($25 one-time)
1. 2.Create app and upload key
1. 3.Build with eas build --platform android
1. 4.Upload AAB to Play Console
1. 5.Submit for review (few hours)

## Native Features

Access device capabilities through React Native modules:

### Camera & Photos

- • Take photos
- • Record videos
- • Access photo library
- • Image picker

### Location

- • GPS location
- • Geofencing
- • Maps integration
- • Background location

### Push Notifications

- • Local notifications
- • Remote push
- • Scheduled notifications
- • Badge counts

### Storage

- • AsyncStorage
- • Secure storage
- • File system
- • SQLite database

### Device APIs

- • Accelerometer
- • Biometrics (Face ID, Touch ID)
- • Bluetooth
- • Device info

### Media

- • Audio playback
- • Video player
- • Audio recording
- • Media controls

## Learn More
[### React Native Setup

Development environment and tools](https://www.algorithmshift.ai/docs/mobile/react-native)[### Native Features

Camera, location, notifications, and more](https://www.algorithmshift.ai/docs/mobile/native)[### App Store Deployment

Deploy to Apple App Store and Google Play](https://www.algorithmshift.ai/docs/mobile/deployment)[### Offline Mode

Build offline-first mobile applications](https://www.algorithmshift.ai/docs/mobile/offline)
