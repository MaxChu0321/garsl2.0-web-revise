<template>
  <q-page class="q-pa-md">
    <div class="q-pa-md row justify-center">
      <q-card
        style="width: 60vw;"
        flat
        bordered
      >

        <q-tabs
          v-model="mode"
          dense
          class="text-grey-7"
          active-color="indigo-10"
          indicator-color="deep-orange-8"
          align="justify"
        >
          <q-tab name="case" label="Case" />
          <q-tab name="batch" label="Batch" />
        </q-tabs>

        <!-- <q-tab-panels v-model="mode" animated>
          <q-tab-panel name="case" class="row justify-center">
            <CaseForm />
          </q-tab-panel> -->
          <q-tab-panels v-model="mode" animated>
          <q-tab-panel name="case">
            <div class="row justify-center">
              <case-form v-if="!showResults" @formSubmitted="handleFormSubmission" />
              <case-result-page v-if="showResults" :result="resultData" />
            </div>
          </q-tab-panel>

          <q-tab-panel name="batch" class="row justify-center">
            <div class="col-md-8">
              <BatchForm />
            </div>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>

      <!-- <div class="flex-container">
        <case-form class="form-container"  @formSubmitted="handleFormSubmission" />
        <case-result-page v-if="showResults" :result="resultData" class="result-container" />
      </div> -->
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

// export default defineComponent({
//   name: 'IndexPage',
//   components: {
//     CaseForm,
//     CaseResultPage,
//     BatchForm
//   },
//   setup() {
//     const mode = ref('case')
//     const showResults = ref(false);
//     const resultData = ref(null); // 假设这是结果数据的初始结构

//     // 处理表单提交
//     const handleFormSubmission = (data) => {
//       // 假设data是CaseForm提交的结果数据
//       resultData.value = data;
//       showResults.value = true;
//       mode.value = 'case'
//     }

//     return {
//       mode,
//       showResults,
//       resultData,
//       handleFormSubmission
//     };
//   },
// })
export default defineComponent({
  name: 'IndexPage',
  components: {
    CaseForm,
    // BatchForm,
    CaseResultPage
  },
  setup() {
    const showResults = ref(false);
    const resultData = ref(null);
    // const formClass = computed(() => {
    //   return showResults.value ? 'form-part' : 'full-width';
    // });
    const formClass = computed(() => {
      return showResults.value ? 'half-width' : 'full-width';
    });

    const resultClass = computed(() => {
      return showResults.value ? 'result-part' : 'hide-result';
    });
    function handleFormSubmission(data) {
      showResults.value = true;
      resultData.value = data;
      // 不要清除表单值，只是显示结果
    }
    
    return {
      mode: ref('case'),
      showResults,
      resultData,
      handleFormSubmission,
      formClass,
      resultClass
    };
  }
});
</script>
<style>
.flex-container {
  display: flex;
  flex-direction: row; /* 水平排列 */
  /* justify-content: center; 
  align-items: flex-start;  */
  /* justify-content: space-around; */
  justify-content: space-between;
  align-items: center;
  min-height: 100vh;
  
}

.form-part {
  flex: 1; /* 分配空间，使表单部分占据一半的空间 */
 } 

.result-part {
  /* flex: 1;  */
  width: 50%;
  transition: width 0.3s;
}
.hide-result {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}
.full-width {
  width: 100%;
  
}
.form-container{
  /* flex: 1;
  transition: transform 0.3s;
  transform: translateX(0%); */
  width: 600px; 
  max-width: 100%; 
  /* flex-basis: 50%; */
  /* display: flex; */
  /* justify-content: center;
  align-items: center; */
}

/* .result-container {
  flex: 1;
  transition: width 0.3s;
  width: 600px; 
} */
.half-width {
  flex-basis: 50%;
}
/* 隐藏结果组件直到表单提交 */
case-result-page {
  width: 0;
  overflow: hidden;
  transition: width 0.3s;
}

/* 当结果显示时，我们改变宽度 */
.result-container {
  width: 50%;
}
</style>
