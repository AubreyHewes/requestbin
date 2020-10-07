from flask import make_response, render_template, request, session

import requestbin.config as config
from requestbin import db


def update_recent_bins(name):
    if 'recent' not in session:
        session['recent'] = []
    if name in session['recent']:
        session['recent'].remove(name)
    session['recent'].insert(0, name)
    if len(session['recent']) > 10:
        session['recent'] = session['recent'][:10]
    session.modified = True


def expand_recent_bins():
    if 'recent' not in session:
        session['recent'] = []
    recent = []
    for name in session['recent']:
        try:
            recent.append(db.lookup_bin(name))
        except KeyError:
            session['recent'].remove(name)
            session.modified = True
    return recent


def home():
    return render_template('home.html', recent=expand_recent_bins())


def bin(name):
    try:
        bin = db.lookup_bin(name)
    except KeyError:
        return "Not found\n", 404
    if request.query_string.decode() == 'inspect':
        if bin.private and session.get(bin.name) != bin.secret_key:
            return "Private bin\n", 403
        update_recent_bins(name)
        return render_template('bin.html',
                               bin=bin,
                               base_url=request.scheme+'://'+request.host,
                               MAX_REQUESTS=config.MAX_REQUESTS,
                               BIN_TTL=config.BIN_TTL / 3600)
    else:

        db.create_request(bin, request)
        resp = make_response("ok\n")
        return resp


def docs(name):
    doc = db.lookup_doc(name)
    if doc:
        return render_template('doc.html',
                               content=doc['content'],
                               title=doc['title'],
                               recent=expand_recent_bins())
    else:
        return "Not found", 404
