import { ref, reactive, readonly  } from "vue"
export function useTestCase(){
  const demo_case = reactive({
    'tumor_size': 2.7,
    'lnast': 4.25,
    'tumor_number': 2,
    'ishak': 6,
    'height': 168,
    'weight': 56.9,
    'steatosis_grade': 0,
    'k': 3.6,
    'ast': 70,
    'hbsag': 1,
    'mvi': 0,
    // 'albigrade': 2,
    'bclc': 1,
    'histologic_grade': 3,
    'afp': 151,
    'bili': 0.57,
    'alb': 3.7,
    // 'bmi':20.16,
    // 'steatosis_grade2': 0,
      
  })

  return { demo_case:readonly(demo_case) }
}
