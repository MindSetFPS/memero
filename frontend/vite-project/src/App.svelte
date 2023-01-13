<script>
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
  import { onMount } from 'svelte';

  let posts = []

  onMount(async function(){
    const response = await fetch('/images')
    const data = response.json()
    posts = data
  })
  
</script>

<main>
  <h1 class="text-5xl font-bold">Hola</h1>
  <form action="/" method="post" enctype="multipart/form-data">

    <input type="file" id="myFile" name="file">
    <input type="submit" value="Upload">
  
  </form>
  <div>

    {#each posts as post}
      {post.url}
    {/each}
    
  </div>
</main>
