# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LinkPost'
        db.create_table('collins_linkpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['LinkPost'])

        # Adding model 'CodePost'
        db.create_table('collins_codepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['CodePost'])

        # Adding model 'Blog'
        db.create_table('collins_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('collins', ['Blog'])

        # Adding M2M table for field admins on 'Blog'
        db.create_table('collins_blog_admins', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['collins.blog'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('collins_blog_admins', ['blog_id', 'user_id'])

        # Adding model 'ChatPost'
        db.create_table('collins_chatpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('chat', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['ChatPost'])

        # Adding model 'QuotePost'
        db.create_table('collins_quotepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('quote_author', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['QuotePost'])

        # Adding model 'ImagePost'
        db.create_table('collins_imagepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['ImagePost'])

        # Adding model 'AudioPost'
        db.create_table('collins_audiopost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('audio', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['AudioPost'])

        # Adding model 'VideoExternalPost'
        db.create_table('collins_videoexternalpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('embed_code', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['VideoExternalPost'])

        # Adding model 'VideoFilePost'
        db.create_table('collins_videofilepost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('collins', ['VideoFilePost'])

        # Adding model 'Theme'
        db.create_table('collins_theme', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('collins', ['Theme'])

        # Adding model 'TextPost'
        db.create_table('collins_textpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['collins.Blog'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('collins', ['TextPost'])


    def backwards(self, orm):
        
        # Deleting model 'LinkPost'
        db.delete_table('collins_linkpost')

        # Deleting model 'CodePost'
        db.delete_table('collins_codepost')

        # Deleting model 'Blog'
        db.delete_table('collins_blog')

        # Removing M2M table for field admins on 'Blog'
        db.delete_table('collins_blog_admins')

        # Deleting model 'ChatPost'
        db.delete_table('collins_chatpost')

        # Deleting model 'QuotePost'
        db.delete_table('collins_quotepost')

        # Deleting model 'ImagePost'
        db.delete_table('collins_imagepost')

        # Deleting model 'AudioPost'
        db.delete_table('collins_audiopost')

        # Deleting model 'VideoExternalPost'
        db.delete_table('collins_videoexternalpost')

        # Deleting model 'VideoFilePost'
        db.delete_table('collins_videofilepost')

        # Deleting model 'Theme'
        db.delete_table('collins_theme')

        # Deleting model 'TextPost'
        db.delete_table('collins_textpost')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'collins.audiopost': {
            'Meta': {'object_name': 'AudioPost'},
            'audio': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.blog': {
            'Meta': {'object_name': 'Blog'},
            'admins': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'collins.chatpost': {
            'Meta': {'object_name': 'ChatPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'chat': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.codepost': {
            'Meta': {'object_name': 'CodePost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.imagepost': {
            'Meta': {'object_name': 'ImagePost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'collins.linkpost': {
            'Meta': {'object_name': 'LinkPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'collins.quotepost': {
            'Meta': {'object_name': 'QuotePost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_author': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.textpost': {
            'Meta': {'object_name': 'TextPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.theme': {
            'Meta': {'object_name': 'Theme'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'template': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'collins.videoexternalpost': {
            'Meta': {'object_name': 'VideoExternalPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'collins.videofilepost': {
            'Meta': {'object_name': 'VideoFilePost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['collins.Blog']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'time_posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['collins']
