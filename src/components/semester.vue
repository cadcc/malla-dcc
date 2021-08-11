<template>
  <div
    class="flex flex-col items-center justify-center md:flex-row md:justify-start"
  >
    <div
      class="mb-4 text-center uppercase md:transform md:-rotate-90 md:-translate-x-1/8 md:mb-0"
    >
      <p>Semestre</p>
      <p>{{ number }}</p>
    </div>
    <div
      class="flex flex-wrap items-center justify-center mb-2 md:flex-row md:justify-start"
    >
      <subject
        v-for="(subject, index) in subjects"
        :key="index"
        :name="subject.name"
        :code="subject.code"
        :requirements="subject.requirements"
        class="mb-2 mr-2"
      >
      </subject>
    </div>
  </div>
</template>

<script>
import Subject from './subject';
export default {
  components: {
    Subject,
  },
  props: {
    subjects: {
      type: Array,
      required: true,
    },
    number: {
      type: Number,
      required: true,
    },
  },
};
</script>
