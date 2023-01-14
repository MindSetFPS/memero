<script>
    export let tags
    let taglist = tags.split(",")
</script>

<div class="flex" >
    {#each taglist as tag}
    <p class="hover:bg-orange-500 p-2">
        {tag}
    </p>
    {/each}
</div>
