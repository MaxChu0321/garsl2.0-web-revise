<template>
  <q-list class="col-md-5 bg-transparent" bordered padding>
    <!-- ... 其他 q-item ... -->

    <q-item v-for="(value, key) in job_store.originalFormValues" :key="key" class="row items-center">
      <q-item-section class="col-3">{{ key }}</q-item-section>
      <q-item-section class="col-3">-</q-item-section> <!-- Reference Interval -->
      <q-item-section class="col-3">{{ value }}</q-item-section>
      <q-item-section class="col-3">
        <div class="status-indicators">
          <div class="status-circle red" v-show="getStatusClass(value) === 'high'"></div>
          <div class="status-circle yellow" v-show="getStatusClass(value) === 'medium'"></div>
          <div class="status-circle green" v-show="getStatusClass(value) === 'low'"></div>
        </div>
      </q-item-section>
    </q-item>
  </q-list>
</template>

<script>
import { defineComponent } from 'vue';
import { useJobStore } from 'src/stores/job';

export default defineComponent({
  name: 'YourComponentName',
  setup() {
    const job_store = useJobStore();

    function getStatusClass(value) {
      // 你的逻辑来决定状态
      if (value > ... ) return 'high';
      if (value > ... ) return 'medium';
      return 'low';
    }

    return {
      job_store,
      getStatusClass,
    };
  }
});
</script>

<style>
.status-indicators {
  display: flex;
}

.status-circle {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 4px;
}

.status-circle.red {
  background-color: #FF0000;
}

.status-circle.yellow {
  background-color: #FFFF00;
}

.status-circle.green {
  background-color: #00FF00;
}
</style>
