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
          
          <!-- <q-btn
            unelevated
            color="teal-6"
            label="Toggle Result"
            @click="toggleResults"
            class="q-mt-md"
          /> -->
        </div>
        <case-result-page v-show="showResults" class="result-part" :result="resultData" />
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import CaseForm from 'src/components/CaseForm.vue';
import BatchForm from 'src/components/BatchForm.vue';
import CaseResultPage from 'src/pages/CaseResultPage.vue';
// import { ref } from 'vue';

export default defineComponent({
  name: 'IndexPage',
  components: {
    CaseForm,
    CaseResultPage,
    BatchForm,
  },
  setup() {
    const mode = ref('case');
    const showResults = ref(false);
    const resultData = ref(null); // 假设这是结果数据的初始结构
    const formValues = ref(null); // 存储表单的当前值

    // 处理表单提交
    const handleFormSubmission = (data) => {
      formValues.value = data.originalFormValues 
      // 假设data是CaseForm提交的结果数据
      resultData.value = data;
      showResults.value = true;
      mode.value = 'case'
      updateResponsiveStyle();
    };
   

    return {
      mode,
      showResults,
      resultData,
      handleFormSubmission,
      formValues,
    };
  },
});
</script>

<style>
.flex-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: stretch;
  width: 100%;
}

/* .form-part {
  flex: 1;  
  max-width: 70%;
  width: 50%;
  display: flex;
  flex-direction: column; 
  justify-content: flex-start;
  align-items: flex-start;
} */
.form-part {
  max-width: 100%;
  width: 100%;
  margin-right: -250px; /* 负 margin 使得右侧没有留白 */
  margin-left: -40px; /* 负 margin 使得左侧没有留白 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.result-part {
  /* flex: 1; */
  width: 65%;
  margin-right: -140px;
  margin-left: -40px;
  /* transition: margin-left 0.3s; */
  /* display: flex; */
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
}
/* .form-part {

  max-width: 100%;
  width: 70%;
 
  justify-content: flex-start; 
  align-items: flex-start; 

 }  */

/* .result-part {

  width: 50%;
  transition: width 0.3s;

  justify-content: center; 
  align-items: center; 
  
} */

.hide-result {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}

.full-width {
  width: 100%;
}

.q-mt-md {
  margin-top: 1rem;
}

/* 隐藏结果组件直到表单提交 */
case-result-page {
  width: 100%;
  overflow: hidden;
  transition: width 0.3s;
}
</style>
