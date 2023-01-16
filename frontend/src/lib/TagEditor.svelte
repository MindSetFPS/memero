<div>
    TagEditor
    <input type="text" name="tag" id="tag" on:keypress={addTag} bind:value={value} >

</div>

<script>
    import getBaseUrl from "./getBaseUrl";
    export let id;
    let value;

    let baseUrl = getBaseUrl()

    async function addTag(event){
        if(event.keyCode == 13){
            const res = await fetch(`${baseUrl}/image/edit/${id}`, {
                method: "POST",
                body: JSON.stringify({
                    tags: value
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            const text = await res.json();

            console.log(text)
            
        }
    }
</script>