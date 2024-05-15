<template>
  <q-form
      @submit="submitForm"
      class="q-gutter-md custom-bg"
    >
      <div class="row q-gutter-md">
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.1" v-model="form.tumor_size" label=" Tumor size (cm)" 
        :rules="[val => (val >= 0 && val <= 10) || 'Value must be between 0 and 10']"/>
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.tumor_number" label=" Tumor number" 
        :rules="[val => Number.isInteger(Number(val)) || 'Value must be an integer']"/>
        <!-- <q-input outlined color="indigo-9" type="number" step="0.01" v-model="form.bmi" label="BMI" /> -->
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.height" label=" Height (cm)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.weight" label=" Weight (kg)" />
        
      </div>
      <div class="row q-gutter-md">
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.steatosis_grade" label="Steatosis grade" /> -->
        
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.ast" label=" AST (U/L)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="1" v-model="form.afp" label=" AFP (ng/mL)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.bili" label=" Bilirubin (mg/dL)" />
        <q-input class="custom-label-spacing"  outlined color="indigo-9" type="number" step="0.01" v-model="form.alb" label=" Albumin (g/dL)" />
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.hbsag" label="HBsAg" /> -->
      </div>
      <!-- <div class="row q-gutter-md"> -->
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.mvi" label="Microvascular invasion" /> -->
        <!-- <q-input outlined color="indigo-9" type="number" step="0.1" v-model="form.histologic_grade" label="Histologic grade" /> -->
        <!-- <q-input outlined color="indigo-9" type="number" step="1" v-model="form.afp" label="AFP(ng/mL)" /> -->
        <!-- <q-input outlined color="indigo-9" type="number" step="0.01" v-model="form.steatosis_grade2" label="Steatosis grade2" /> -->
      <!-- </div> -->

      <div class="row q-gutter-md">
        <q-input class="custom-label-spacing" outlined color="indigo-9" type="number" step="0.1" v-model="form.k" label="K (mmol/L)" />
            <!-- <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            ALBIgrade
            <q-option-group
                :options="[
                { label: 'I', value: 0, color: 'green' },
                { label: 'II', value: 1, color: 'yellow' },
                { label: 'III', value: 2, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.albigrade"
            />
            </div> -->
        
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            BCLC stage
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: 'A', value: 1, color: 'yellow' },
                { label: 'B', value: 2, color: 'orange' },
                { label: 'C', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.bclc"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Steatosis grade
            <q-option-group
                :options="[
                { label: 'None', value: 0, color: 'green' },
                { label: 'Mild', value: 1, color: 'yellow' },
                { label: 'Moderate', value: 2, color: 'orange' },
                { label: 'Severe', value: 3, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.steatosis_grade"
            />
            </div>
            </div>
            <div class="row q-gutter-md">
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Microvascular invasion
            <q-option-group
                :options="[
                { label: 'Absence', value: 0, color: 'green' },
                { label: 'Presence', value: 1, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.mvi"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            HBsAg
            <q-option-group
                :options="[
                { label: 'Negative', value: 0, color: 'green' },
                { label: 'Positive', value: 1, color: 'red' }
                ]"
                type="radio"
                inline
                v-model="form.hbsag"
            />
            </div>
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Histologic grade
            <q-option-group
                :options="[
                { label: '1', value: 1, color: 'green' },
                { label: '2', value: 2, color: 'yellow' },
                { label: '3', value: 3, color: 'orange' },
                { label: '4', value: 4, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.histologic_grade"
            />
            </div>
            
            </div>
            <div class="row q-gutter-md">
            <div class="q-pa-sm rounded-borders" :class="$q.dark.isActive ? 'bg-grey-9' : 'bg-grey-2'">
            Ishak fibrosis stage
            <q-option-group
                :options="[
                { label: '0', value: 0, color: 'green' },
                { label: '1', value: 1, color: 'yellow' },
                { label: '2', value: 2, color: 'yellow' },
                { label: '3', value: 3, color: 'orange' },
                { label: '4', value: 4, color: 'orange' },
                { label: '5', value: 5, color: 'red' },
                { label: '6', value: 6, color: 'red' },
                ]"
                type="radio"
                inline
                v-model="form.ishak"
            />
            </div>
            

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
      'height': null,
      'weight': null,
      'bili': null,
      'alb': null,
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
      form.height= demo_case.height
      form.weight= demo_case.weight
      form.bili= demo_case.bili
      form.alb= demo_case.alb
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

    const calculateBMI = () => {
      const heightInMeters = form.height / 100;
      const weightInKg = form.weight;
      form.bmi = heightInMeters > 0 && weightInKg > 0
        ? (weightInKg / (heightInMeters * heightInMeters)).toFixed(2)
        : null;
    };

    const calALBiscore = () => {
      const bilirubin_mg_per_dL = form.bili;
      const albumin_g_per_dL = form.alb;
      const bilirubin_umol_per_L_conversion = 17.1;
      const albumin_g_per_L_conversion = 10;
      const bilirubin_umol_per_L = bilirubin_mg_per_dL * bilirubin_umol_per_L_conversion;
      const albumin_g_per_L = albumin_g_per_dL * albumin_g_per_L_conversion;
      const albi_score = Math.log10(bilirubin_umol_per_L) * 0.66 + albumin_g_per_L * (-0.085)
      if (albi_score <= -2.60) {
          form.albigrade = 1;
        }
      if (albi_score > -2.60 && albi_score <= -1.39) {
          form.albigrade = 2;
        }
      if (albi_score > -1.39) {
          form.albigrade = 3;
        }
    };



    const submitForm = () =>{
      calculateBMI();
      calALBiscore();
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
.custom-label-spacing .q-field__label {
  padding-left: 8px; /* 或任何你需要的間距 */
}

</style>