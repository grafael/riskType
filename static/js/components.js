Vue.component('britecore-component', {
  delimiters: ['[[', ']]'],
  props: ['label', 'val', 'type', 'required'],
  template: '#britecore-component-template',
  data: () => ({
    date: null,
    modal: false,
    en: null,
    numberRules:[v => !isNaN(v) || 'Must be a number !']
  }),
})
