# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Posts.slug'
        db.delete_column(u'posts_posts', 'slug')


    def backwards(self, orm):
        # Adding field 'Posts.slug'
        db.add_column(u'posts_posts', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2014, 6, 21, 0, 0), max_length=50),
                      keep_default=False)


    models = {
        u'posts.posts': {
            'Meta': {'object_name': 'Posts'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['posts']