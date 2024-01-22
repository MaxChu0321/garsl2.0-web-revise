<template>
  <q-btn
    label="Download the example file"
    color="teal-6"
    unelevated
    @click="downloadExcelFile"
  />
</template>

<script>
export default {
  name: 'DownloadExampleButton',
  setup () {
    const downloadExcelFile = () =>{
      const link = document.createElement('a')
      link.href = 'example.xlsx'
      link.setAttribute('download', 'example.xlsx')
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
    return {downloadExcelFile}
  }
}
</script>
