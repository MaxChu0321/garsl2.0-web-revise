<template>
  <q-form
      @submit="submitForm"
      class="q-gutter-md custom-bg"
    >
      <div class="row q-gutter-md">
        <q-input outlined color="indigo-9" type="number" step="0.1" v-model="form.tumor_size" label="Tumor size" 
        :rules="[val => (val >= 0 && val <= 10) || 'Value must be between 0 and 10']"/>
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.tumor_number" label="Tumor number" 
        :rules="[val => Number.isInteger(Number(val)) || 'Value must be an integer']"/>
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.ishak" label="Ishak fibrosis stage" 
        :rules="[val => Number.isInteger(Number(val)) || 'Value must be an integer']"/>
        <q-input outlined color="indigo-9" type="number" step="0.01" v-model="form.bmi" label="BMI" />
      </div>
      <div class="row q-gutter-md">
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.steatosis_grade" label="Steatosis grade" />
        <q-input outlined color="indigo-9" type="number" step="0.1" v-model="form.k" label="K" />
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.ast" label="AST" />
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.hbsag" label="HBsAg" />
      </div>
      <div class="row q-gutter-md">
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.mvi" label="Microvascular invasion" />
        <q-input outlined color="indigo-9" type="number" step="0.1" v-model="form.histologic_grade" label="Histologic grade" />
        <q-input outlined color="indigo-9" type="number" step="1" v-model="form.afp" label="AFP" />
        <!-- <q-input outlined color="indigo-9" type="number" step="0.01" v-model="form.steatosis_grade2" label="Steatosis grade2" /> -->
      </div>
      <div class="row q-gutter-md">
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            ALBIgrade
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.albigrade"
            />
            </div>
        
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            BCLC stage
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'orange' },
                { label: '3', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.bclc"
            />
            </div>
            <!-- <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            class_Histologic grade
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'orange' },
                { label: '3', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.class_histologic_grade"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            class_AFP
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'orange' },
                { label: '3', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.class_afp"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            class_Steatosis grade
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.class_steatosis_grade"
            />
            </div> -->
        </div>
        <div class="row q-gutter-md justify-end">
            <q-btn unelevated color="teal-6" type="button" label="Clear" @click="reloadPage" />
            <q-btn unelevated color="teal-6" type="button" label="Demo" @click="demo" />
            <q-btn unelevated color="teal-6" type="submit" label="Submit" />
        </div>
    </q-form>
</template>

<script>
import { defineComponent, reactive, ref , getCurrentInstance, watch, toRefs} from 'vue'
import { api } from "boot/axios"
import { useRouter } from 'vue-router'
import { useJobStore } from 'stores/job'
import { useTestCase } from '../helpers/useDemo'

export default defineComponent({
  name: 'CaseForm',
  emits: ['formSubmitted'],
  props: {
    initialValues: {
      type: Object,
      default: () => ({})
    }
  },
  setup (props, { emit }) {
    const $router = useRouter()
    const job_store = useJobStore()
    const { initialValues } = toRefs(props)
    let { demo_case } = useTestCase()
    // console.log(demo_case)

    const form = reactive({
      'tumor_size': null,
      // 'lnast': null,
      'tumor_number': null,
      'ishak': null,
      'bmi': null,
      'steatosis_grade': null,
      'k': null,
      'ast': null,
      'hbsag': null,
      'mvi': null,
      'albigrade': null,
      'bclc': null,
      'histologic_grade': null,
      'afp': null,
      // 'steatosis_grade2': null,
      
    })
    // const form = reactive({
    //   tumor_size: props.initialValues.tumor_size || null,
    //   tumor_number: props.initialValues.tumor_number || null,
    //   ishak: props.initialValues.ishak || null,
    //   height: props.initialValues.height || null,
    //   steatosis_grade: props.initialValues.steatosis_grade || null,
    //   k: props.initialValues.k || null,
    //   ast: props.initialValues.ast || null,
    //   hbsag: props.initialValues.hbsag || null,
    //   mvi: props.initialValues.mvi || null,
    //   albigrade: props.initialValues.albigrade || null,
    //   bclc: props.initialValues.bclc || null,
    //   histologic_grade: props.initialValues.histologic_grade || null,
    //   afp: props.initialValues.afp || null,
    //   // 你可以继续为其他字段添加默认值
    // })

    const initForm = () => {
      for (const key in initialValues.value) {
        if (form.hasOwnProperty(key)) {
          form[key] = initialValues.value[key]
        }
      }
    }
    
    watch(initialValues, (newValues) => {
      initForm();
    }, { deep: true })

    // 在组件挂载时初始化表单
    initForm();
    const demo = () => {
      form.tumor_size= demo_case.tumor_size,
      // form.lnast= demo_case.lnast,
      form.tumor_number= demo_case.tumor_number,
      form.ishak= demo_case.ishak,
      form.bmi= demo_case.bmi,
      form.steatosis_grade= demo_case.steatosis_grade,
      form.k= demo_case.k,
      form.ast= demo_case.ast,
      form.hbsag= demo_case.hbsag,
      form.mvi= demo_case.mvi,
      form.albigrade= demo_case.albigrade,
      form.bclc= demo_case.bclc,
      form.histologic_grade= demo_case.histologic_grade,
      form.afp= demo_case.afp
      // form.steatosis_grade2= demo_case.steatosis_grade2
    }

    const checkValidity = (fieldName, min, max) => {
      const inputValue = form.value[fieldName];
      const isValid = inputValue >= min && inputValue <= max;

      if (!isValid) {
        const inputRef = this.$refs[`${fieldName}Input`];
        if (inputRef) {
          inputRef.showValidationMessage(`Please enter a value between ${min} and ${max}`);
        }
      }
    };
    const submitForm = () =>{
      api.post("submit/case", form)
        .then((response)=>{
          job_store.updateJobResult(response.data[0])
          job_store.updateOriginalFormValues(form)
          console.log(job_store.risk_score)
          // Emit an event instead of navigating
          emit('formSubmitted', {
          originalFormValues: form,
          predictionResult: response.data[0]
          // $router.push('/result/case')
        });
      })
        .catch((error)=>{
          console.log(error.message)
        })
    }

    const reloadPage = () => {
      // 重新加載當前頁面
      // location.reload();
      $router.go(0); /* 這個方法會比較smooth*/
    };

    return {form, submitForm, demo,reloadPage }
  }
})
</script>
<style>
.custom-bg {
  background-color: rgba(255, 255, 255, 0.7); /* 白色背景，50% 透明度 */
}
</style>