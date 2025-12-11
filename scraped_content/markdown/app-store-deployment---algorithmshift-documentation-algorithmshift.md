# App Store Deployment - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/deployment  
**Scraped:** 2025-12-10 14:03:26

**Description:** Deploy your mobile apps to Apple App Store and Google Play Store.

---

App Store Deployment - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# App Store Deployment

Publish your mobile apps to Apple App Store and Google Play Store.

### Apple App Store

iOS deployment

#### Prerequisites

- • Apple Developer account ($99/year)
- • App Store Connect access
- • macOS with Xcode

#### Build & Submit
Copy
```
# Build iOS app
eas build --platform ios --profile production

# Submit to App Store
eas submit --platform ios

# Or manually via Xcode
# 1. Archive app
# 2. Upload to App Store Connect
# 3. Submit for review
```

#### Review Process

- • App review: 1-3 days
- • Approval or rejection
- • Address feedback if rejected
- • Resubmit and repeat

### Google Play Store

Android deployment

#### Prerequisites

- • Google Play Console ($25 one-time)
- • Signed upload key
- • Android SDK

#### Build & Submit
Copy
```
# Build Android app
eas build --platform android --profile production

# Submit to Play Store
eas submit --platform android

# Or manually via Play Console
# 1. Create app bundle (AAB)
# 2. Upload to Play Console
# 3. Submit for review
```

#### Review Process

- • App review: Few hours to 1 day
- • Faster than iOS
- • Address feedback if needed
- • Publish when approved
