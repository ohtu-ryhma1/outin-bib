types = {
    "article": {
        "required": ["author", "title", "journaltitle", "year/date"],
        "optional": ["translator", "annotator", "commentator", "subtitle", "titleaddon",
                    "editor", "editora", "editorb", "editorc", "journalsubtitle",
                    "journaltitleaddon", "issuetitle", "issuesubtitle", "issuetitleaddon",
                    "language", "origlanguage", "series", "volume", "number", "eid", "issue",
                    "month", "pages", "version", "note", "issn", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "book": {
        "required": ["author", "title", "year/date"],
        "optional": ["editor", "editora", "editorb", "editorc", "translator", "annotator",
                    "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "maintitle", "mainsubtitle", "maintitleaddon", "language",
                    "origlanguage", "volume", "part", "edition", "volumes", "series", "number",
                    "note", "publisher", "location", "isbn", "eid", "chapter", "pages", "pagetotal",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype",
                    "url", "urldate"]
    },

    "mvbook": {
        "required": ["author", "title", "year/date"],
        "optional": ["editor", "editora", "editorb", "editorc", "translator", "annotator",
                    "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "language", "origlanguage", "edition", "volumes", "series",
                    "number", "note", "publisher", "location", "isbn", "pagetotal", "addendum",
                    "pubstate", "doi", "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "inbook": {
        "required": ["author", "title", "booktitle", "year/date"],
        "optional": ["bookauthor", "editor", "editora", "editorb", "editorc", "translator",
                    "annotator", "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "maintitle", "mainsubtitle", "maintitleaddon", "booksubtitle",
                    "booktitleaddon", "language", "origlanguage", "volume", "part", "edition",
                    "volumes", "series", "number", "note", "publisher", "location", "isbn", "eid",
                    "chapter", "pages", "addendum", "pubstate", "doi", "eprint", "eprintclass",
                    "eprinttype", "url", "urldate"]
    },

    "bookinbook": {
        "required": ["author", "title", "booktitle", "year/date"],
        "optional": ["editor", "editora", "editorb", "editorc", "translator", "annotator",
                    "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "maintitle", "mainsubtitle", "maintitleaddon", "language",
                    "origlanguage", "volume", "part", "edition", "volumes", "series", "number",
                    "note", "publisher", "location", "isbn", "eid", "chapter", "pages", "pagetotal",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype",
                    "url", "urldate"]
    },

    "suppbook": {
        "required": ["booktitle", "year/date"],
        "optional": ["author", "title", "bookauthor", "editor", "editora", "editorb", "editorc",
                    "translator", "annotator", "commentator", "introduction", "foreword",
                    "afterword", "subtitle", "titleaddon", "maintitle", "mainsubtitle",
                    "maintitleaddon", "booksubtitle", "booktitleaddon", "language", "origlanguage",
                    "volume", "part", "edition", "volumes", "series", "number", "note", "publisher",
                    "location", "isbn", "eid", "chapter", "pages", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "booklet": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "howpublished", "type", "note",
                    "location", "eid", "chapter", "pages", "pagetotal", "addendum", "pubstate",
                    "doi", "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "collection": {
        "required": ["editor", "title", "year/date"],
        "optional": ["editora", "editorb", "editorc", "translator", "annotator", "commentator",
                    "introduction", "foreword", "afterword", "subtitle", "titleaddon",
                    "maintitle", "mainsubtitle", "maintitleaddon", "language", "origlanguage",
                    "volume", "part", "edition", "volumes", "series", "number", "note",
                    "publisher", "location", "isbn", "eid", "chapter", "pages", "pagetotal",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype", "url",
                    "urldate"]
    },

    "mvcollection": {
        "required": ["editor", "title", "year/date"],
        "optional": ["editora", "editorb", "editorc", "translator", "annotator", "commentator",
                    "introduction", "foreword", "afterword", "subtitle", "titleaddon", "language",
                    "origlanguage", "edition", "volumes", "series", "number", "note", "publisher",
                    "location", "isbn", "pagetotal", "addendum", "pubstate", "doi", "eprint",
                    "eprintclass", "eprinttype", "url", "urldate"]
    },

    "incollection": {
        "required": ["author", "title", "editor", "booktitle", "year/date"],
        "optional": ["editor", "editora", "editorb", "editorc", "translator", "annotator",
                    "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "maintitle", "mainsubtitle", "maintitleaddon", "booksubtitle",
                    "booktitleaddon", "language", "origlanguage", "volume", "part", "edition",
                    "volumes", "series", "number", "note", "publisher", "location", "isbn", "eid",
                    "chapter", "pages", "addendum", "pubstate", "doi", "eprint", "eprintclass",
                    "eprinttype", "url", "urldate"]
    },

    "suppcollection": {
        "required": ["booktitle", "year/date"],
        "optional": ["author", "title", "bookauthor", "editor", "editora", "editorb", "editorc",
                    "translator", "annotator", "commentator", "introduction", "foreword",
                    "afterword", "subtitle", "titleaddon", "maintitle", "mainsubtitle",
                    "maintitleaddon", "booksubtitle", "booktitleaddon", "language", "origlanguage",
                    "volume", "part", "edition", "volumes", "series", "number", "note", "publisher",
                    "location", "isbn", "eid", "chapter", "pages", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "dataset": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "edition", "type", "series", "number",
                    "version", "note", "organization", "publisher", "location", "addendum",
                    "pubstate", "doi", "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "manual": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "edition", "type", "series", "number",
                    "version", "note", "organization", "publisher", "location", "isbn", "eid",
                    "chapter", "pages", "pagetotal", "addendum", "pubstate", "doi", "eprint",
                    "eprintclass", "eprinttype", "url", "urldate"]
    },

    "misc": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "howpublished", "type", "version",
                    "note", "organization", "location", "month", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "online": {
        "required": ["author", "editor", "title", "year/date", "doi", "eprint", "url"],
        "optional": ["subtitle", "titleaddon", "language", "version", "note", "organization",
                    "month", "addendum", "pubstate", "eprintclass", "eprinttype", "urldate"]
    },

    "patent": {
        "required": ["author", "title", "number", "year/date"],
        "optional": ["holder", "subtitle", "titleaddon", "type", "version", "location", "note",
                    "month", "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype",
                    "url", "urldate"]
    },

    "periodical": {
        "required": ["editor", "title", "year/date"],
        "optional": ["editora", "editorb", "editorc", "subtitle", "titleaddon", "issuetitle",
                    "issuesubtitle", "issuetitleaddon", "language", "series", "volume", "number",
                    "issue", "month", "note", "issn", "addendum", "pubstate", "doi", "eprint",
                    "eprintclass", "eprinttype", "url", "urldate"]
    },

    "suppperiodical": {
        "required": ["author", "title", "journaltitle", "year/date"],
        "optional": ["translator", "annotator", "commentator", "subtitle", "titleaddon", "editor", 
                    "editora", "editorb", "editorc", "journalsubtitle", "journaltitleaddon",
                    "issuetitle", "issuesubtitle", "issuetitleaddon", "language", "origlanguage",
                    "series", "volume", "number", "eid", "issue", "month", "pages", "version",
                    "note", "issn", "addendum", "pubstate", "doi", "eprint", "eprintclass",
                    "eprinttype", "url", "urldate"]
    },

    "proceedings": {
        "required": ["title", "year/date"],
        "optional": ["editor", "subtitle", "titleaddon", "maintitle", "mainsubtitle",
                    "maintitleaddon", "eventtitle", "eventtitleaddon", "eventdate", "venue",
                    "language", "volume", "part", "volumes", "series", "number", "note",
                    "organization", "publisher", "location", "month", "isbn", "eid", "chapter",
                    "pages", "pagetotal", "addendum", "pubstate", "doi", "eprint", "eprintclass",
                    "eprinttype", "url", "urldate"]
    },

    "mvproceedings": {
        "required": ["title", "year/date"],
        "optional": ["editor", "subtitle", "titleaddon", "eventtitle", "eventtitleaddon",
                    "eventdate", "venue", "language", "volumes", "series", "number", "note",
                    "organization", "publisher", "location", "month", "isbn", "pagetotal",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype",
                    "url", "urldate"]
    },

    "inproceedings": {
        "required": ["author", "title", "booktitle", "year/date"],
        "optional": ["editor", "subtitle", "titleaddon", "maintitle", "mainsubtitle",
                    "maintitleaddon", "booksubtitle", "booktitleaddon", "eventtitle",
                    "eventtitleaddon", "eventdate", "venue", "language", "volume", "part",
                    "volumes", "series", "number", "note", "organization", "publisher", "location",
                    "month", "isbn", "eid", "chapter", "pages", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "reference": {
        "required": ["editor", "title", "year/date"],
        "optional": ["editora", "editorb", "editorc", "translator", "annotator", "commentator",
                    "introduction", "foreword", "afterword", "subtitle", "titleaddon",
                    "maintitle", "mainsubtitle", "maintitleaddon", "language", "origlanguage",
                    "volume", "part", "edition", "volumes", "series", "number", "note",
                    "publisher", "location", "isbn", "eid", "chapter", "pages", "pagetotal",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype", "url",
                    "urldate"]
    },

    "mvreference": {
        "required": ["editor", "title", "year/date"],
        "optional": ["editora", "editorb", "editorc", "translator", "annotator", "commentator",
                    "introduction", "foreword", "afterword", "subtitle", "titleaddon", "language",
                    "origlanguage", "edition", "volumes", "series", "number", "note", "publisher",
                    "location", "isbn", "pagetotal", "addendum", "pubstate", "doi", "eprint",
                    "eprintclass", "eprinttype", "url", "urldate"]
    },

    "inreference": {
        "required": ["author", "title", "editor", "booktitle", "year/date"],
        "optional": ["editor", "editora", "editorb", "editorc", "translator", "annotator",
                    "commentator", "introduction", "foreword", "afterword", "subtitle",
                    "titleaddon", "maintitle", "mainsubtitle", "maintitleaddon", "booksubtitle",
                    "booktitleaddon", "language", "origlanguage", "volume", "part", "edition",
                    "volumes", "series", "number", "note", "publisher", "location", "isbn", "eid",
                    "chapter", "pages", "addendum", "pubstate", "doi", "eprint", "eprintclass",
                    "eprinttype", "url", "urldate"]
    },

    "report": {
        "required": ["author", "title", "type", "institution", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "number", "version", "note", "location",
                    "month", "isrn", "eid", "chapter", "pages", "pagetotal", "addendum", "pubstate",
                    "doi", "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "software": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "howpublished", "type", "version",
                    "note", "organization", "location", "month", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

    "thesis": {
        "required": ["author", "title", "type", "institution", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "note", "location", "month", "isbn",
                    "eid", "chapter", "pages", "pagetotal", "addendum", "pubstate", "doi", "eprint",
                    "eprintclass", "eprinttype", "url", "urldate"]
    },

    "unpublished": {
        "required": ["author", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "type", "eventtitle", "eventtitleaddon", "eventdate",
                    "venue", "language", "howpublished", "note", "location", "isbn", "month",
                    "addendum", "pubstate", "doi", "eprint", "eprintclass", "eprinttype", "url",
                    "urldate"]
    },

    "custom[a-f]": {
        "required": ["author/editor", "title", "year/date"],
        "optional": ["subtitle", "titleaddon", "language", "howpublished", "type", "version",
                    "note", "organization", "location", "month", "addendum", "pubstate", "doi",
                    "eprint", "eprintclass", "eprinttype", "url", "urldate"]
    },

}
