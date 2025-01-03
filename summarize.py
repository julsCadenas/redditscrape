from transformers import BartForConditionalGeneration, BartTokenizer

class Summarize:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    def summarize(self, text, prompt):
        inputs = self.tokenizer.encode(
            f"{prompt}: {text}",
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )
        summary_ids = self.model.generate(
            inputs,
            max_length=130,
            min_length=30,
            length_penalty=2.0,
            num_beams=4,
            # no_repeat_ngram_size=3,
            # early_stopping=True
        )
        summary = self.tokenizer.decode(
            summary_ids[0], 
            skip_special_tokens=True
        )
        return summary

    def process_data(self, response, prompt):
        post_content = response[0]['data']['children'][0]['data'].get('selftext', '')
        comments = []
        for comment in response[1]['data']['children']:
            if 'body' in comment['data']:
                comments.append(comment['data']['body'])
        comments_all = ' '.join(comments)

        post_summary = self.summarize(post_content, prompt)
        comments_summary = self.summarize(comments_all, prompt)

        return {
            "post_summary": post_summary,
            "comments_summary": comments_summary
        }