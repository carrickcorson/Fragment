let messages = [];

            function sendMessage(){
                let input = document.getElementById("input");
                let chatDiv = document.getElementById("chat");
                let text = input.value;

                messages.push({role: "user", content: text});

                chatDiv.innerHTML += "<article>\n<b>You:\n</b> " + text + "</article>";
                chatDiv.scrollTo(0, chatDiv.scrollHeight);

                input.value = "";

                fetch("/api/chat", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({messages: messages})
                })
                .then(res => {
                    let article = document.createElement("article");
                    let responseText = document.createElement("div");
                    article.innerHTML = "<b>Fragment:</b>";
                    article.appendChild(responseText);
                    chatDiv.appendChild(article);

                    let fullText = "";
                    const reader = res.body.getReader();
                    const decoder = new TextDecoder();

                    function read() {
                        reader.read().then(({done, value}) => {
                            if (done) {
                                messages.push({"role": "assistant", "content": fullText});
                                return;
                            }

                            const lines = decoder.decode(value).split("\n");
                            for (const line of lines) {
                                if (line.startsWith("data: ")) {
                                    const data = line.slice(6);
                                    if (data === "[DONE]") return;
                                    try {
                                        fullText += JSON.parse(data).chunk;
                                        responseText.innerHTML = marked.parse(fullText);
                                        const distance_from_bottom = chatDiv.scrollHeight - chatDiv.scrollTop - chatDiv.clientHeight;

                                        if (distance_from_bottom < 100) {
                                            chatDiv.scrollTo(0, chatDiv.scrollHeight)
                                        }
                                    } catch(e) {}
                                }
                            }

                            read();
                        });
                    }

                    read();
                });
            }


            document.getElementById("input").addEventListener("keydown", function(event) {
                if (event.key === "Enter" && !event.shiftKey) {
                    event.preventDefault();
                    sendMessage();
                }
            });