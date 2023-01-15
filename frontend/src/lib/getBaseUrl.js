export default function getBaseUrl(){
    if (import.meta.env.PROD){
      return ''
    } else {
      return 'http://127.0.0.1:5000'
    }
  }