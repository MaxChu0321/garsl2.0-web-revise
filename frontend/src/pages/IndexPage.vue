<template>
  <q-page class="q-pa-md">
    <div class="row justify-center">
      <!-- 使用 v-if 来决定是否显示 card -->
      <q-card v-if="!showResults" class="q-pa-md column justify-center" flat bordered>
        <q-tabs v-model="mode" dense class="text-grey-7" active-color="indigo-10" indicator-color="deep-orange-8" align="justify">
          <q-tab name="case" label="Case" />
          <q-tab name="batch" label="Batch" />
        </q-tabs>

        <q-tab-panels v-model="mode" animated>
          <q-tab-panel name="case">
            <case-form @formSubmitted="handleFormSubmission"  />
          </q-tab-panel>
          <q-tab-panel name="batch">
            <batch-form />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>

      <!-- 这里处理结果显示 -->
      <div v-if="showResults" class="flex-container full-width">
        <div class="col" align="center">
          <case-form class="form-part" :initial-values="formValues" />
          <case-result-page class="result-part" :result="resultData" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, reactive, ref,computed } from 'vue'
import CaseForm from "src/components/CaseForm.vue"
import BatchForm from 'src/components/BatchForm.vue'
import CaseResultPage from 'src/pages/CaseResultPage.vue'
// export default defineComponent({
//   name: 'IndexPage',
//   components: {
//     CaseForm,
//     BatchForm
//   },
//   setup() {
//     return {
//       mode: ref('case')
//     }
//   },
// })

export default defineComponent({
  name: 'IndexPage',
  components: {
    CaseForm,
    CaseResultPage,
    BatchForm
  },
  setup() {
    const mode = ref('case')
    const showResults = ref(false);
    const resultData = ref(null); // 假设这是结果数据的初始结构
    const formValues = ref(null) // 存储表单的当前值
    
    // 处理表单提交
    const handleFormSubmission = (data) => {
      formValues.value = data.originalFormValues 
      // 假设data是CaseForm提交的结果数据
      resultData.value = data;
      showResults.value = true;
      mode.value = 'case'
    }

    return {
      mode,
      showResults,
      resultData,
      handleFormSubmission,
      formValues
    };
  },
})
</script>
<style>
.flex-container {
  display: flex;
  flex-direction: row; 
  /* justify-content: center; 
  align-items: flex-start;  */
  /* justify-content: space-around; */
  justify-content: space-between;
  align-items: center;
  /* min-height: 100vh; */
  
}

.form-part {
  /* flex: 1;  */
  width: 50%;
  /* display: flex;  */
  justify-content: center; 
  align-items: center; 

 } 

.result-part {
  /* flex: 1;  */
  width: 50%;
  transition: width 0.3s;
  /* display: flex;  */
  justify-content: center; 
  align-items: center; 
  
}

.hide-result {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}
.full-width {
  width: 100%;
  
}
/* 隐藏结果组件直到表单提交 */
case-result-page {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}

</style>
