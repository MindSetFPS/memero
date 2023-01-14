<script>
  import Tag from "./lib/Tag.svelte";
import Tags from "./lib/Tags.svelte";

  
	async function getImages() {
    const res = await fetch(`http://127.0.0.1:5000/images`);
		const text = await res.json();
    
		if (res.ok) {
      console.log(text)
			return text;
		} else {
      throw new Error(text);
		}
	}
  
  function getBaseUrl(){
    if (import.meta.env.PROD){
      return ''
    } else {
      return 'http://127.0.0.1:5000'
    }
  }
  
  async function handleUpload(){
    console.log(files)
    const formData = new FormData()
    formData.append('file', files[0])
    formData.append('tags', tags)
    
    console.log(tags)
    
    const res = await fetch(baseUrl + '/', {
      method: 'POST',
      body: formData
    })
    
    const text = await res.json()
    
    if (res.ok) {
      return text;
		} else {
      throw new Error(text);
		}
  }
  
  let posts;
  let files;
  let tags;
  let promise = getImages()
  let baseUrl = getBaseUrl()
</script>

<main>
  <h1 class="text-5xl font-bold">Hola</h1>
  <form action="/" method="post" enctype="multipart/form-data" on:submit|preventDefault={handleUpload} >
    <input type="file" id="myFile" name="file" bind:files >
    <input type="submit" value="Upload">
    <Tags bind:value={tags} on:tag={() => console.log(tags)} />
  </form>
  <div>
    {#await promise}
      <h1>Loading</h1>
    {:then promise}
    {#each promise as post}
      <img src="{baseUrl}/image/{post.filename}" alt="">
      <div class="flex">
        {post.filename}
        <Tag tags={post.tags} />
      </div>
      {/each}
    {/await}
  </div>
</main>
