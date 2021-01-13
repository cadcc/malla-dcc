<template>
  <div :class="{ dark: $store.state.darkMode }">
    <div
      class="flex flex-col items-center justify-center dark:bg-gray-700 dark:text-white"
    >
      <toggle class="ml-auto" :value="$store.state.darkMode" />
      <p class="my-4 text-3xl font-bold text-center">
        Malla DCC 💻 (vieja 🧓👴)
      </p>
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
          <div class="flex flex-row items-center mr-4">
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
import malla from '../public/malla.json';
import Semester from './components/semester';
import Toggle from './components/toggle';

export default {
  name: 'App',
  components: {
    Semester,
    Toggle,
  },
  data() {
    return {
      semesters: malla.semesters,
    };
  },
};
</script>
