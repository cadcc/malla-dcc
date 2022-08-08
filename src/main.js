import { createApp, h } from 'vue';
import { createLogger, createStore } from 'vuex';
import App from './App.vue';
import './css/application.css';

const store = createStore({
  state() {
    return {
      mallaActiva: 'mallav5',
      darkMode:
        window.matchMedia &&
        window.matchMedia('(prefers-color-scheme: dark)').matches
          ? true
          : false,
      activeSubject: '',
      simultaneousSubjects: [],
      orSubjects: [],
      requiredSubjects: [],
    };
  },
  mutations: {
    setActiveSubject: (state, payload) => {
      state.activeSubject = payload;
    },
    setSimultaneousSubjects: (state, payload) => {
      state.simultaneousSubjects = payload;
    },
    setOrSubjects: (state, payload) => {
      state.orSubjects = payload;
    },
    setRequiredSubjects: (state, payload) => {
      state.requiredSubjects = payload;
    },
    setDarkMode: (state, payload) => {
      state.darkMode = payload;
    },
    setMalla: (state, payload) => {
      state.mallaActiva = payload;
    },
  },
  actions: {
    clearActiveSubject: context => {
      context.commit('setActiveSubject', '');
      context.commit('setSimultaneousSubjects', []);
      context.commit('setOrSubjects', []);
    },
    toggleDarkMode: context => {
      context.commit('setDarkMode', !context.state.darkMode);
    },
    toggleMalla: context => {
      const newValue =
        context.state.mallaActiva === 'mallav3' ? 'mallav5' : 'mallav3';
      context.commit('setMalla', newValue);
    },
  },
  plugins: [createLogger()],
});

const app = createApp({
  render: () => h(App),
});
app.config.devtools = true;
app.use(store);
app.mount('#app');
