## Base

```bash
git clone git@github.com:lis-space/flood-test.git
cd flood-test
pip install -r requirements.txt
```

## Server

```bash
python server.py
```

## Client

Mode 1. Finding final page in redirects chain.

```bash
python client.py -m 1
```

Mode 2. Infinite redirects chain.

```bash
python client.py -m 2
```

Mode 3. Infinite redirects chain.

```bash
python client.py -m 3
```

## License

MIT.
