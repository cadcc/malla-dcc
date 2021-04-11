<template>
  <div :class="{ dark: $store.state.darkMode }">
    <div
      class="flex flex-col items-center justify-center dark:bg-gray-700 dark:text-white"
    >
      <toggle
        @toggle="$store.dispatch('toggleDarkMode')"
        id="darkMode"
        active-text="🌙"
        non-active-text="☀️"
        class="ml-auto"
        :value="$store.state.darkMode"
      />
      <div class="flex my-4 text-3xl font-bold text-center">
        <p>
          Malla DCC 💻
          <span>{{
            $store.state.mallaActiva === 'mallav3'
              ? '(vieja 🧓👴)'
              : '(nueva👧👦)'
          }}</span>
        </p>
      </div>
      <p>Versión malla</p>
      <toggle
        class="mb-4"
        @toggle="$store.dispatch('toggleMalla')"
        id="malla"
        active-text="v3"
        non-active-text="v5"
        :value="$store.state.mallaActiva === 'mallav3'"
      />
      <div>
        <div class="flex flex-col items-center mb-4 md:flex-row">
          <div class="flex flex-row items-center mr-4">
            <div
              class="w-8 h-4 mr-1 bg-green-300 border-2 border-black dark:bg-green-800 dark:border-white"
            ></div>
            <span>Ramo activo</span>
          </div>
          <div class="flex flex-row items-center mr-4">
            <div
              class="w-8 h-4 mr-1 bg-blue-300 border-4 border-black border-double dark:bg-blue-800 dark:border-white"
            ></div>
            <span>Ramo requerido</span>
          </div>
          <div
            class="flex flex-row items-center mr-4"
            v-if="$store.state.mallaActiva === 'mallav3'"
          >
            <div
              class="w-8 h-4 mr-1 bg-yellow-300 border-2 border-black border-dotted dark:bg-yellow-600 dark:border-white"
            ></div>
            <span>Ramos simultáneos</span>
          </div>
          <div class="flex flex-row items-center mr-4">
            <div
              class="w-8 h-4 mr-1 bg-red-300 border-2 border-black border-dashed dark:bg-red-800 dark:border-white"
            ></div>
            <span>Ramos "or" (se necesita uno)</span>
          </div>
        </div>
      </div>
      <div>
        <semester
          v-for="(semester, index) in semesters"
          :key="index"
          :subjects="semester.subjects"
          :number="semester.number"
        >
          {{ semester }}
        </semester>
      </div>
    </div>
  </div>
</template>

<script>
import mallav3 from '../public/mallav3.json';
import mallav5 from '../public/mallav5.json';
import Semester from './components/semester';
import Toggle from './components/toggle';

export default {
  name: 'App',
  components: {
    Semester,
    Toggle,
  },
  computed: {
    semesters(){
      return this.$store.state.mallaActiva === 'mallav3'
        ? mallav3.semesters
        : mallav5.semesters;
    }
  }
};
</script>
