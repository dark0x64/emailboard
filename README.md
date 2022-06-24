# emailboard
Image board software for static hosting on Neocities which uses e-mail to create threads and reply to them.

Only POP3 is supported.

## Usage
Send e-mail to the set address in this format
```
Subject: CreateThread ["Thread name"]
Description...
```

```
Subject: ReplyThread <Thread number>
Description...
```

### Examples
```
Subject: CreateThread "Cats"
I love cats!
```

```
Subject: CreateThread
I don't like dogs.
```

```
Subject: ReplyThread 346
Yes, indeed, verily.
That is indeed very true.
Surely.
```
