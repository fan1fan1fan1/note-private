import { createApp } from 'vue'
import router from './router'
import { createPinia } from 'pinia';
import App from './App.vue'

import piniaPersist from 'pinia-plugin-persitedstate'

pinia.use(piniaPersist);   // 持久化插件
const app = createApp(App)
const pinia = createPinia();

app.use(pinia);
app.use(router)

app.mount('#app')
