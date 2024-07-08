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
                <th class="text-left">Months</th>
                <th class="text-center">6</th>
                <th class="text-center">12</th>
                <th class="text-center">18</th>
                <th class="text-center">24</th>
                <!-- <th class="text-center">5</th>  -->
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-left">Survival rate</td>
                <!-- <td class="text-center">{{ job_store.survival_rates[0] }}</td> -->
                <td class="text-center">{{ formatPercentage(job_store.survival_rates[0]) }}</td>
                <td class="text-center">{{ formatPercentage(job_store.survival_rates[1]) }}</td>
                <td class="text-center">{{ formatPercentage(job_store.survival_rates[2]) }}</td>
                <td class="text-center">{{ formatPercentage(job_store.survival_rates[3]) }}</td>
                <!-- <td class="text-center">{{ formatPercentage(job_store.survival_rates[4]) }}</td> -->
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
          <!-- <Bar id="survival-chart" :options="chart_options" :data="survival_data" :plugins="chart_plugins"/> -->

        </q-card-section>
      </q-card>
    </div>

  </q-page>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js'
import { useJobStore } from 'stores/job'
import { computed } from 'vue';
import Chart from 'chart.js/auto';
// ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
ChartJS.register(Title, Tooltip, Legend, BarElement, LineElement, CategoryScale, LinearScale, PointElement)

export default {
  name: 'CaseResultPage',
  components: { Bar  },
  setup() {
    const job_store = useJobStore()

    // const survival_data = computed(() => ({
    //   labels: ["1 year", "2 year","3 year", "4 year", "5 year"],
    //   datasets: [
    //     {
    //       label: "Survival rate",
    //       // data: job_store.survival_rates,
    //       data: job_store.survival_rates.map(rate => rate * 100),
    //       backgroundColor: '#1976d2',
    //     },
    //     {
    //       type: 'line',
    //       label: 'Survival Trend',
    //       data: job_store.survival_rates.map(rate => rate * 100),
    //       borderColor: '#f87979',
    //       fill: false,
    //       tension: 0.1, // 這會讓線條稍微彎曲
    //       pointBackgroundColor: '#f87979',
    //       pointBorderColor: '#fff'
    //     }
    //   ],
    // }))

    const survival_data = computed(() => ({
      labels: ["6 month", "12 month", "18 month", "24 month"],
      datasets: [
        {
          type: 'bar',
          label: 'Survival rate',
          data: job_store.survival_rates.map(rate => rate * 100),
          backgroundColor: '#1976d2',
          order:2,
        },
        {
          type: 'line',
          label: '',
          data: job_store.survival_rates.map(rate => rate * 100),
          borderColor: '#f87979',
          borderWidth: 3,
          fill: false,
          tension: 0.5, // 調整曲線的彎曲程度
          pointBackgroundColor: '#f87979',
          pointBorderColor: '#fff',
          pointBorderWidth: 2,
          pointRadius: 5,
          order:1,
        }
      ],
    }));

    const chart_options = {
      responsive: true,

      plugins: {
        legend: {
          display: true,
          labels: {
            filter: function(item, chart) {
              // 只顯示有標籤的數據集
              return item.text !== '';
            }
          }
        }
      },

      scales: {
        y: {
          beginAtZero: true,
          suggestedMax: 100,
          
          title: {
          display: true,
          text: 'Recurrence-free survival (%)', // 這裡設定你想顯示的標籤文字
          color: '#666', // 可以設定標籤文字顏色
          font: {
          size: 14, // 設定文字大小
          family: 'Arial' // 設定字體
        }
      }}}
    };
    function getStatusClass(value) {
      // 根据 value 决定返回哪个 CSS 类
      if (value > 90) return 'high';
      if (value > 50) return 'medium';
      return 'low';
    }
    function formatPercentage(value) {
      return `${(value * 100).toFixed(0)}%`; // 轉換為整數百分比
    }
    return {job_store, survival_data, chart_options,getStatusClass, formatPercentage}
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