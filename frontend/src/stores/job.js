import { defineStore } from 'pinia'

export const useJobStore = defineStore('job', {
  state: () => ({
    risk_score: null,
    risk_group: null,
    survival_rates: null,
    formValues: null,
  }),

  getters: {
    get2yprob: (state) =>{ return state.survival_rates[3] },
    // get3yprob: (state) =>{ return formValues[2] },
  },

  actions: {
    updateJobResult (res) {
      this.risk_score = res.risk_score;
      this.risk_group = res.risk_group;
      this.survival_rates = res.survival_rates;
      this.formValues = res;
    },
    updateOriginalFormValues(formValues) {
      this.originalFormValues = formValues;}
  }
})
