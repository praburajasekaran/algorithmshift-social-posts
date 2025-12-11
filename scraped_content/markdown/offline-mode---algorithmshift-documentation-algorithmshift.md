# Offline Mode - AlgorithmShift Documentation | AlgorithmShift

**URL:** https://www.algorithmshift.ai/docs/mobile/offline  
**Scraped:** 2025-12-10 14:03:27

**Description:** Build offline-first mobile applications with local storage and sync.

---

Offline Mode - AlgorithmShift Documentation | AlgorithmShiftDocumentationMobile Apps
# Offline Mode

Build apps that work offline. Store data locally and sync when connection is restored.

### Local Storage

AsyncStorage, SQLite

### Auto Sync

Background sync

### Offline Queue

Queue operations

### Conflict Resolution

Handle data conflicts

## Implementing Offline Support
Copy
```
import AsyncStorage from '@react-native-async-storage/async-storage';
import NetInfo from '@react-native-community/netinfo';

// Check network status
const isConnected = await NetInfo.fetch();

if (isConnected.isConnected) {
  // Online: Fetch from API
  const data = await fetchFromAPI();
  // Cache locally
  await AsyncStorage.setItem('tasks', JSON.stringify(data));
} else {
  // Offline: Load from cache
  const cached = await AsyncStorage.getItem('tasks');
  const data = JSON.parse(cached);
}

// Queue offline operations
const queueOperation = async (operation) => {
  const queue = await AsyncStorage.getItem('offline_queue') || '[]';
  const operations = JSON.parse(queue);
  operations.push(operation);
  await AsyncStorage.setItem('offline_queue', JSON.stringify(operations));
};

// Sync when online
NetInfo.addEventListener(state => {
  if (state.isConnected) {
    syncOfflineQueue();
  }
});
```
