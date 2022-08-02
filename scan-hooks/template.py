# A template scan hook (https://www.zaproxy.org/docs/docker/scan-hooks/)
# Note that not all hooks will be called in all scans.

def cli_opts(opts):
	print(f"cli_opts({opts})")

def zap_started(zap, target):
	print(f"zap_started({zap}, {target})")

def importing_openapi(target_url, target_file):
	print(f"importing_openapi({target_url}, {target_file})")

def importing_soap(target_url, target_file):
	print(f"importing_soap({target_url}, {target_file})")

def load_config(config, config_dict, config_msg, out_of_scope_dict):
	print(
		f"load_config({config}, {config_dict}, {config_msg}, {out_of_scope_dict})"
	)

def print_rules_wrap(count, inprog_count):
	print(f"print_rules_wrap({count}, {inprog_count})")

def start_zap(port, extra_zap_params):
	print(f"start_zap({port}, {extra_zap_params})")

def start_docker_zap(docker_image, port, extra_zap_params, mount_dir):
	print(
		f"start_docker_zap({docker_image}, {port}, {extra_zap_params}, {mount_dir})"
	)

def start_docker_zap_wrap(cid):
	print(f"start_docker_zap_wrap({cid})")

def zap_access_target(zap, target):
	print(f"zap_access_target({zap}, {target})")

def zap_spider(zap, target):
	print(f"zap_spider({zap}, {target})")

def zap_spider_wrap(unused):
	print("zap_spider_wrap(unused)")

def zap_ajax_spider(zap, target, max_time):
	print(f"zap_ajax_spider({zap}, {target}, {max_time})")

def zap_ajax_spider_wrap(unused):
	print("zap_ajax_spider_wrap(unused)")

def zap_active_scan(zap, target, policy):
	print(f"zap_active_scan({zap}, {target}, {policy})")

def zap_active_scan_wrap(unused):
	print("zap_active_scan_wrap(unused)")

def zap_get_alerts(zap, baseurl, denylist, out_of_scope_dict):
	print(f"zap_get_alerts({zap}, {baseurl}, {denylist}, {out_of_scope_dict})")

def zap_get_alerts_wrap(alert_dict):
	print(f"zap_get_alerts_wrap({alert_dict})")

def zap_import_context(zap, context_file):
	print(f"zap_import_context({zap}, {context_file})")

def zap_import_context_wrap(context_id):
	print(f"zap_import_context_wrap({context_id})")

def zap_pre_shutdown(zap):
	print(f"zap_pre_shutdown({zap})")

def pre_exit(fail_count, warn_count, pass_count):
	print(f"pre_exit({fail_count}, {warn_count}, {pass_count})")

