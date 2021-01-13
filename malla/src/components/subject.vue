<template>
  <div
    @mouseover="activateSubject"
    @click="activateSubject"
    @mouseleave="$store.dispatch('clearActiveSubject')"
    class="flex flex-col items-center justify-center w-48 p-4 h-28"
    :class="activeClass"
  >
    <p class="text-center">{{ name }}</p>
    <p>{{ code }}</p>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    code: {
      type: String,
      required: true,
    },
    requirements: {
      type: Array,
      required: true,
    },
  },
  methods: {
    activateSubject() {
      const simultaneousSubjects = this.requirements.filter(subject =>
        subject.includes('S')
      );
      const orSubjectsStrings = this.requirements.filter(subject =>
        subject.includes('/')
      );
      const requiredSubjects = this.requirements.filter(
        subject => !subject.includes('S') && !subject.includes('/')
      );
      const orSubjects = orSubjectsStrings.map(str => str.split('/'));
      this.$store.commit('setActiveSubject', this.code);
      this.$store.commit('setSimultaneousSubjects', simultaneousSubjects);
      this.$store.commit('setOrSubjects', orSubjects);
      this.$store.commit('setRequiredSubjects', requiredSubjects);
    },
  },
  computed: {
    activeClass() {
      if (this.$store.state.activeSubject === this.code) {
        return 'bg-green-300 dark:bg-green-800 border-2 border-black dark:border-white';
      }
      if (
        this.$store.state.orSubjects.some(subject =>
          subject.includes(this.code)
        )
      ) {
        return 'bg-red-300 dark:bg-red-800 border-2 border-black border-dashed dark:border-white';
      }
      if (
        this.$store.state.simultaneousSubjects.some(subject =>
          subject.startsWith(this.code)
        )
      ) {
        return 'bg-yellow-300 dark:bg-yellow-600 border-2 border-black border-dotted dark:border-white';
      }
      if (
        this.$store.state.requiredSubjects.some(subject =>
          subject.startsWith(this.code)
        )
      ) {
        return 'bg-blue-300 dark:bg-blue-800 border-4 border-black border-double dark:border-white';
      }
      return this.$store.state.activeSubject
        ? 'dark:bg-gray-800 bg-gray-300 opacity-50 dark:opacity-75'
        : 'dark:bg-gray-800 bg-gray-300 border-double';
    },
  },
};
</script>
