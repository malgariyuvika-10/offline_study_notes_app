# Data Schema

## JSON Structure

```json
{
  "title": "",
  "summary": "",
  "topics": [
    {
      "heading": "",
      "key_points": [],
      "examples": []
    }
  ],
  "flashcards": [
    {
      "question": "",
      "answer": ""
    }
  ]
}
```

## SQLite Schema

### Notes

| Column | Type |
|----------|------|
| id | INTEGER |
| title | TEXT |
| filename | TEXT |
| created_at | DATETIME |
| json_output | TEXT |

## History

| Column | Type |
|----------|------|
| id | INTEGER |
| note_id | INTEGER |
| timestamp | DATETIME |