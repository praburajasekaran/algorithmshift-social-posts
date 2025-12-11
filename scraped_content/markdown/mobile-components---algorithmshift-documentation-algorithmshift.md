# Mobile Components - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/components  
**Scraped:** 2025-12-10 14:04:01

**Description:** 21 native React Native components for building mobile apps. Complete reference with properties and examples.

---

Mobile Components - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# Mobile Components

Complete library of 21 native React Native components for building iOS and Android apps. Each component is optimized for touch interactions and mobile performance.

### Mobile-First Components

When you create a mobile app (app.type === 'mobile'), the component drawer automatically shows these React Native components instead of web components. No conversion needed!

## Component Categories

### Mobile Layout (4 components)

Container and layout components for structuring your mobile app

#### View

Basic container component. The fundamental building block for mobile UI.
Copy
```
<View style={{ padding: 16, backgroundColor: '#fff' }}>
  <Text>Content goes here</Text>
</View>
```

Common Properties:

- • style - Styling (flexbox, padding, margin, colors)
- • onLayout - Called when layout changes

#### ScrollView

Scrollable container for content that exceeds screen size.
Copy
```
<ScrollView 
  horizontal={false}
  showsVerticalScrollIndicator={true}
  refreshControl={<RefreshControl refreshing={false} />}
>
  <View>{/* Long content */}</View>
</ScrollView>
```

Common Properties:

- • horizontal - Horizontal scrolling (default: false)
- • showsVerticalScrollIndicator - Show scroll indicator
- • refreshControl - Pull-to-refresh component

#### SafeAreaView

Automatically applies padding to avoid device notches, status bar, and home indicator.
Copy
```
<SafeAreaView style={{ flex: 1, backgroundColor: '#fff' }}>
  <View>{/* Your app content */}</View>
</SafeAreaView>
```

Use Cases:

- • iPhone X+ notch avoidance
- • Status bar clearance
- • Home indicator spacing (iOS)

#### KeyboardAvoidingView

Automatically adjusts view when keyboard appears to prevent input fields from being hidden.
Copy
```
<KeyboardAvoidingView 
  behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
  style={{ flex: 1 }}
>
  <TextInput placeholder="Email" />
  <TextInput placeholder="Password" />
</KeyboardAvoidingView>
```

Common Properties:

- • behavior - "height" | "padding" | "position"
- • keyboardVerticalOffset - Additional offset

### Mobile Basic (5 components)

Essential UI components for text, buttons, and feedback

#### Text

Display text content with styling.
Copy
```
<Text 
  style={{ fontSize: 16, fontWeight: 'bold', color: '#333' }}
  numberOfLines={2}
  ellipsizeMode="tail"
>
  This is some text content
</Text>
```

Common Properties:

- • numberOfLines - Truncate after N lines
- • ellipsizeMode - "head" | "middle" | "tail" | "clip"
- • selectable - Allow text selection (default: false)

#### TouchableOpacity

Touchable button with opacity feedback. Most common button component.
Copy
```
<TouchableOpacity 
  activeOpacity={0.7}
  onPress={() => console.log('Pressed!')}
  disabled={false}
  style={{ padding: 12, backgroundColor: '#007AFF', borderRadius: 8 }}
>
  <Text style={{ color: '#fff', textAlign: 'center' }}>
    Click Me
  </Text>
</TouchableOpacity>
```

Common Properties:

- • activeOpacity - Opacity when pressed (0-1, default: 0.2)
- • onPress - Function called on press
- • disabled - Disable touch interactions
- • hitSlop - Extend touchable area

#### Pressable

Advanced touchable with more control over press states.
Copy
```
<Pressable 
  onPress={() => {}}
  onPressIn={() => {}}
  onPressOut={() => {}}
  onLongPress={() => {}}
  style={({ pressed }) => [
    { padding: 12 },
    pressed && { opacity: 0.5 }
  ]}
>
  {({ pressed }) => (
    <Text>{pressed ? 'Pressed!' : 'Press me'}</Text>
  )}
</Pressable>
```

#### Image

Display images from local or remote sources.
Copy
```
<Image 
  source={{ uri: 'https://example.com/image.jpg' }}
  style={{ width: 200, height: 200 }}
  resizeMode="cover"
/>

{/* Local image */}
<Image 
  source={require('./assets/logo.png')}
  style={{ width: 100, height: 100 }}
/>
```

Resize Modes:

- • cover - Scale to fill, crop if needed
- • contain - Scale to fit, letterbox if needed
- • stretch - Stretch to fill (distort)
- • repeat - Tile the image
- • center - Center without scaling

#### ActivityIndicator

Loading spinner for async operations.
Copy
```
<ActivityIndicator 
  size="large"
  color="#007AFF"
  animating={true}
/>
```

Common Properties:

- • size - "small" | "large" | number
- • color - Spinner color
- • animating - Show/hide spinner

### Mobile Input (2 components)

Form input components optimized for mobile

#### TextInput

Text input field with mobile keyboard types and validation.
Copy
```
{/* Email input */}
<TextInput 
  placeholder="Enter email"
  value={email}
  onChangeText={setEmail}
  keyboardType="email-address"
  autoCapitalize="none"
  autoCorrect={false}
  style={{ borderWidth: 1, padding: 12, borderRadius: 8 }}
/>

{/* Password input */}
<TextInput 
  placeholder="Password"
  value={password}
  onChangeText={setPassword}
  secureTextEntry={true}
  maxLength={50}
/>

{/* Multiline text */}
<TextInput 
  placeholder="Description"
  multiline={true}
  numberOfLines={4}
  textAlignVertical="top"
/>
```

Keyboard Types:

- • default - Standard keyboard
- • email-address - Email keyboard with @
- • numeric - Number pad
- • phone-pad - Phone number pad
- • number-pad - Number pad (no decimal)
- • decimal-pad - Number pad with decimal
- • url - URL keyboard with .com

Auto Capitalize:

- • none - No capitalization
- • sentences - First letter of sentences
- • words - First letter of each word
- • characters - All characters

#### Switch

Toggle switch for boolean values. Native iOS/Android styling.
Copy
```
<Switch
  value={isEnabled}
  onValueChange={setIsEnabled}
  trackColor={{ false: '#767577', true: '#81b0ff' }}
  thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
  ios_backgroundColor="#3e3e3e"
/>
```

Common Properties:

- • value - Boolean state
- • onValueChange - Callback when toggled
- • trackColor - Color for on/off track
- • thumbColor - Color of the thumb
- • disabled - Disable interactions

### Mobile Data (2 components)

Performant lists with virtualization

#### FlatList

Performant scrollable list with virtualization. Only renders visible items.
Copy
```
<FlatList
  data={items}
  renderItem={({ item }) => (
    <View style={{ padding: 16, borderBottomWidth: 1 }}>
      <Text>{item.title}</Text>
    </View>
  )}
  keyExtractor={(item) => item.id}
  horizontal={false}
  numColumns={1}
  onEndReached={() => loadMore()}
  onEndReachedThreshold={0.5}
  refreshing={isRefreshing}
  onRefresh={() => refresh()}
  ListEmptyComponent={<Text>No items</Text>}
  ListHeaderComponent={<Text>Header</Text>}
  ListFooterComponent={<Text>Footer</Text>}
/>
```

Common Properties:

- • data - Array of items
- • renderItem - Function to render each item
- • keyExtractor - Unique key for each item
- • horizontal - Horizontal scrolling
- • numColumns - Grid layout (number of columns)
- • onEndReached - Infinite scroll callback
- • refreshing - Pull-to-refresh state
- • onRefresh - Pull-to-refresh callback

#### SectionList

List with section headers. Perfect for grouped data.
Copy
```
<SectionList
  sections={[
    {
      title: 'Section 1',
      data: ['Item 1', 'Item 2']
    },
    {
      title: 'Section 2',
      data: ['Item 3', 'Item 4']
    }
  ]}
  renderItem={({ item }) => <Text>{item}</Text>}
  renderSectionHeader={({ section }) => (
    <Text style={{ fontWeight: 'bold', padding: 8 }}>
      {section.title}
    </Text>
  )}
  keyExtractor={(item, index) => item + index}
/>
```

### Mobile Navigation (3 components)

Navigation patterns for mobile apps

#### TabNavigator

Bottom tab navigation (iOS) or top tabs (Android). Most common mobile navigation pattern.
Copy
```
// Bottom tabs configuration
{
  type: 'TabNavigator',
  tabs: [
    { name: 'Home', icon: 'home', screen: 'HomeScreen' },
    { name: 'Search', icon: 'search', screen: 'SearchScreen' },
    { name: 'Profile', icon: 'user', screen: 'ProfileScreen' }
  ],
  position: 'bottom',
  activeColor: '#007AFF',
  inactiveColor: '#8E8E93'
}
```

#### StackNavigator

Stack-based navigation with push/pop. Includes back button and gestures.
Copy
```
// Stack navigation configuration
{
  type: 'StackNavigator',
  screens: [
    { name: 'List', component: 'ListScreen' },
    { name: 'Details', component: 'DetailsScreen' },
    { name: 'Edit', component: 'EditScreen' }
  ],
  headerMode: 'float',
  gestureEnabled: true
}
```

#### DrawerNavigator

Side drawer/hamburger menu navigation. Swipe from edge to open.
Copy
```
// Drawer navigation configuration
{
  type: 'DrawerNavigator',
  screens: [
    { name: 'Home', icon: 'home' },
    { name: 'Settings', icon: 'settings' },
    { name: 'Help', icon: 'help-circle' }
  ],
  drawerPosition: 'left',
  drawerType: 'front'
}
```

### Mobile Feedback (2 components)

Modals and alerts for user feedback

#### Modal

Full-screen or partial overlay modal.
Copy
```
<Modal
  visible={isVisible}
  animationType="slide"
  transparent={true}
  onRequestClose={() => setIsVisible(false)}
>
  <View style={{ flex: 1, justifyContent: 'center', backgroundColor: 'rgba(0,0,0,0.5)' }}>
    <View style={{ margin: 20, backgroundColor: 'white', padding: 20, borderRadius: 8 }}>
      <Text>Modal Content</Text>
      <TouchableOpacity onPress={() => setIsVisible(false)}>
        <Text>Close</Text>
      </TouchableOpacity>
    </View>
  </View>
</Modal>
```

Animation Types:

- • slide - Slide from bottom
- • fade - Fade in/out
- • none - No animation

#### Alert

Native alert dialog with buttons (iOS/Android styled).
Copy
```
// Simple alert
Alert.alert(
  'Alert Title',
  'Alert Message',
  [
    { text: 'Cancel', style: 'cancel' },
    { text: 'OK', onPress: () => console.log('OK pressed') }
  ]
);

// Confirmation alert
Alert.alert(
  'Delete Item?',
  'This action cannot be undone.',
  [
    { text: 'Cancel', style: 'cancel' },
    { text: 'Delete', onPress: deleteItem, style: 'destructive' }
  ]
);
```

### Mobile Special (3 components)

Advanced components for native features

#### WebView

Embed web content in your mobile app.
Copy
```
<WebView
  source={{ uri: 'https://example.com' }}
  style={{ flex: 1 }}
  onLoad={() => console.log('Loaded')}
  onError={(error) => console.error(error)}
/>
```

#### MapView

Display interactive maps (requires react-native-maps).
Copy
```
<MapView
  style={{ flex: 1 }}
  initialRegion={{
    latitude: 37.78825,
    longitude: -122.4324,
    latitudeDelta: 0.0922,
    longitudeDelta: 0.0421,
  }}
>
  <Marker
    coordinate={{ latitude: 37.78825, longitude: -122.4324 }}
    title="Marker Title"
  />
</MapView>
```

#### Camera

Access device camera for photos and videos (requires react-native-camera).
Copy
```
<Camera
  style={{ flex: 1 }}
  type={cameraType}
  onCameraReady={() => console.log('Ready')}
>
  <TouchableOpacity onPress={takePicture}>
    <Text>Take Photo</Text>
  </TouchableOpacity>
</Camera>
```

## Using Mobile Components in Builder
1
Create a Mobile App

Set app.type = 'mobile' when creating your app
2
Open App Builder

Component drawer automatically shows mobile components
3
Drag & Drop

Use mobile components just like web components
4
Configure Properties

Set mobile-specific props in the properties panel
5
Preview

Click "App" preview mode to see React Native rendering

## Learn More
[### React Native Setup

Configure your development environment](https://www.algorithmshift.ai/docs/mobile/react-native)[### Mobile Preview

Preview on real devices with QR codes](https://www.algorithmshift.ai/docs/mobile/preview)[### Mobile App Builder

Build mobile apps visually](https://www.algorithmshift.ai/docs/visual-builder/mobile-apps)[### App Store Deployment

Deploy to iOS App Store and Google Play](https://www.algorithmshift.ai/docs/mobile/deployment)
