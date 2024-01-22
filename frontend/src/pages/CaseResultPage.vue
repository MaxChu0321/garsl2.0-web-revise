<template>
  <q-page padding>
    <div class="row justify-center q-gutter-md">
      

      <q-card
        class="col-md-6 custom-bg"
        flat
        bordered
      >
        <q-card-section>
          <q-markup-table :separator="'vertical'" flat bordered>
            <thead>
              <tr>
                <th class="text-left">Years</th>
                <th class="text-right">1</th>
                <th class="text-right">2</th>
                <th class="text-right">3</th>
                <th class="text-right">4</th>
                <th class="text-right">5</th> 
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-left">Survival rate</td>
                <td class="text-right">{{ job_store.survival_rates[0] }}</td>
                <td class="text-right">{{ job_store.survival_rates[1] }}</td>
                <td class="text-right">{{ job_store.survival_rates[2] }}</td>
                <td class="text-right">{{ job_store.survival_rates[3] }}</td>
                <td class="text-right">{{ job_store.survival_rates[4] }}</td>
              </tr>
            </tbody>
          </q-markup-table>
        </q-card-section>

        <q-card-section class="row justify-center">
          <Bar
            id="survival-chart"
            :options="chart_options"
            :data="survival_data"
            :plugins="chart_plugins"
          />
        </q-card-section>
      </q-card>
    </div>

  </q-page>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { useJobStore } from 'stores/job'
import { computed } from 'vue';
import Chart from 'chart.js/auto';
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'CaseResultPage',
  components: { Bar },
  setup() {
    const job_store = useJobStore()

    const survival_data = computed(() => ({
      labels: ["1year", "2year","3year", "4year", "5year"],
      datasets: [
        {
          label: "Survival rate",
          data: job_store.survival_rates,
          backgroundColor: '#1976d2',
        },
      ],
    }))

    const chart_options = {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          suggestedMax: 1
        }
      }
    };
    function getStatusClass(value) {
      // 根据 value 决定返回哪个 CSS 类
      if (value > 90) return 'high';
      if (value > 50) return 'medium';
      return 'low';
    }

    return {job_store, survival_data, chart_options,getStatusClass}
  },

}
</script>
<style>
.status-indicators {
  display: flex;
}
.status-circle {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  margin-right: 4px;
}
.custom-bg {
  background-color: rgba(255, 255, 255, 0.7); /* 白色背景，50% 透明度 */ 
  
}
</style>