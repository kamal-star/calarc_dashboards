## Calarc Dashboards

A tiny Frappe v16 app that adds a **Dashboards** tile to the desk apps screen (`/desk`).
The tile opens the site's `Dashboards` workspace, which lists the dashboards as cards.

The app holds no DocTypes or data. The workspace and its dashboard blocks live on the site,
so they can keep being edited there.

### Install

```bash
bench get-app https://github.com/kamal-star/calarc_dashboards
bench --site <site> install-app calarc_dashboards
```

#### License

MIT
